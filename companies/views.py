from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Sum
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView, DeleteView
from .forms import PaymentForm, UpdatePaymentForm
from .models import Companies, Payment


@login_required(login_url='vrtic:login')
def index_view(request):
    companies = Companies.objects.all()
    payments = Payment.objects.all()

    context = {
        'companies': companies,
        'payments': payments
    }
    return render(request, 'companies/index.html', context)


@login_required(login_url='vrtic:login')
def side_bar(request):
    companies = Companies.objects.all()

    context = {
        'companies': companies,
    }
    return render(request, 'companies/side_bar.html', context)


class CreateCompanyView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Companies
    template_name = 'companies/create_company.html'
    fields = '__all__'
    login_url = 'vrtic:login'
    success_message = 'Kompanija uspjesno dodata'
    success_url = reverse_lazy('companies:index')

    def get_context_data(self, **kwargs):
        kwargs['comp'] = Companies.objects.all()
        return super(CreateCompanyView, self).get_context_data(**kwargs)


class UpdateCompanyView(LoginRequiredMixin, UpdateView):
    model = Companies
    template_name = 'companies/update_company.html'
    fields = '__all__'
    login_url = 'vrtic:login'

    def get_context_data(self, **kwargs):
        kwargs['comp'] = Companies.objects.all()
        return super(UpdateCompanyView, self).get_context_data(**kwargs)

    def get_success_url(self):
        pk = self.kwargs.get('pk')
        messages.info(self.request, 'Podaci uspjesno promijenjeni')
        return reverse_lazy('companies:company_payment', kwargs={'pk': pk})


class DeleteCompanyView(LoginRequiredMixin, DeleteView):
    model = Companies
    login_url = 'vrtic:login'
    success_url = reverse_lazy('companies:index')

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)


@login_required(login_url='vrtic:login')
def company_payment(request, pk):
    companies = Companies.objects.all()
    company = Companies.objects.get(id=pk)
    payments = Payment.objects.filter(company=company)
    total_payment = payments.aggregate(Sum('paid'))
    amount = total_payment.get('paid__sum')
    payment_form = PaymentForm()

    if request.method == 'POST':
        payment_form = PaymentForm(request.POST)
        if payment_form.is_valid():
            payment = payment_form.save(commit=False)
            payment.company = company
            payment_form.save()
            return redirect('companies:company_payment', pk=company.id)

    context = {
        'company': company,
        'payments': payments,
        'amount': amount,
        'payment_form': payment_form,
        'companies': companies,
    }
    return render(request, 'companies/company_payment.html', context)


@login_required(login_url='vrtic:login')
def update_company_payments(request, pk):
    payment = Payment.objects.get(id=pk)
    update_form = UpdatePaymentForm(instance=payment)
    if request.method == 'POST':
        update_form = UpdatePaymentForm(request.POST, instance=payment)
        if update_form.is_valid():
            update_form.save()
            return redirect('companies:company_payment', pk=payment.company.id)

    context = {
        'update_form': update_form,
        'payment': payment
    }
    return render(request, 'companies/modal3.html', context)


@login_required(login_url='vrtic:login')
def delete_payment_company(request, pk):
    payment = Payment.objects.get(id=pk)
    company = payment.company.id
    if request.method == 'POST':
        payment.delete()
        return redirect('companies:company_payment', pk=company)

    context = {
        'payment': payment
    }
    return render(request, 'companies/modal_delete_comp_payment.html', context)


@login_required(login_url='vrtic:login')
def search_company(request):
    companies = Companies.objects.all()
    search = request.GET.get('search_company')
    payments = Payment.objects.filter(payment_date__icontains=search)
    if not payments:
        messages.info(request, 'Pretraga neuspjesna')
        return redirect('companies:index')

    context = {
        'payments': payments,
        'companies': companies
    }
    return render(request, 'companies/index.html', context)



