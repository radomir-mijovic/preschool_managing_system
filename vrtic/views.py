from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.views.generic import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Kids, Group, Payment, Teachers
from .forms import PaymentForm, UpdatePaymentForm
from django.db.models import Sum


def login_user(request):
    if request.user.is_authenticated:
        return redirect('vrtic:kids')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('vrtic:kids')

        messages.info(request, 'Invalid username or password')
        return redirect('vrtic:login')

    return render(request, 'vrtic/login.html')


@login_required(login_url='vrtic:login')
def kids_view(request):
    kids = Kids.objects.all()
    male = Kids.objects.filter(gender='muski').count()
    female = Kids.objects.filter(gender='zenski').count()
    total_kids = Kids.objects.filter().count()
    primary_program = Kids.objects.filter(program_choice='primarni program').count()
    short_program = Kids.objects.filter(program_choice='kraci program').count()

    context = {
        'kids': kids,
        'male': male,
        'female': female,
        'total_kids': total_kids,
        'primary_program': primary_program,
        'short_program': short_program,
    }
    return render(request, 'vrtic/kids_list.html', context)


class CreateKidView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Kids
    template_name = 'vrtic/create.html'
    fields = '__all__'
    login_url = 'vrtic:login'

    def get_context_data(self, **kwargs):
        kwargs['groups'] = Group.objects.all()
        return super(CreateKidView, self).get_context_data(**kwargs)

    def get_success_url(self):
        name = self.request.POST.get('name')
        messages.info(self.request, f"Dijete {name} uspjesno dodato")
        return reverse_lazy('vrtic:kids')


class UpdateKidView(LoginRequiredMixin, UpdateView):
    model = Kids
    fields = '__all__'
    template_name = 'vrtic/update_kid.html'
    login_url = 'vrtic:login'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('vrtic:update_kid', kwargs={'pk': pk})

    def get_context_data(self, **kwargs):
        kwargs['groups'] = Group.objects.all()
        return super(UpdateKidView, self).get_context_data(**kwargs)


class DeleteKidView(LoginRequiredMixin, DeleteView):
    model = Kids
    context_object_name = 'kid'
    login_url = 'vrtic:login'

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

    def get_success_url(self):
        messages.info(self.request, 'Uspjesno brisanje')
        return reverse_lazy('vrtic:kids')


@login_required(login_url='vrtic:login')
def teachers_centralni_view(request):
    teachers = Teachers.objects.filter(group__name__icontains='centr')
    name = 'Centralni Vrtić'

    context = {
        'teachers': teachers,
        'name': name
    }
    return render(request, 'vrtic/teachers.html', context)


@login_required(login_url='vrtic:login')
def teachers_novi_view(request):
    teachers = Teachers.objects.filter(group__name__icontains='novi')
    name = 'Novi Vrtić'

    context = {
        'teachers': teachers,
        'name': name
    }
    return render(request, 'vrtic/teachers.html', context)


@login_required(login_url='vrtic:login')
def teachers_tq_view(request):
    teachers = Teachers.objects.filter(group__name__icontains='tq')
    name = 'TQ Vrtić'

    context = {
        'teachers': teachers,
        'name': name
    }
    return render(request, 'vrtic/teachers.html', context)


@login_required(login_url='vrtic:login')
def teachers_stefan_view(request):
    teachers = Teachers.objects.filter(group__name__icontains='stefan')
    name = 'Sv. Stefan Vrtić'

    context = {
        'teachers': teachers,
        'name': name
    }
    return render(request, 'vrtic/teachers.html', context)


@login_required(login_url='vrtic:login')
def teachers_petrovac_view(request):
    teachers = Teachers.objects.filter(group__name__icontains='petrovac')
    name = 'Petrovac Vrtić'

    context = {
        'teachers': teachers,
        'name': name
    }
    return render(request, 'vrtic/teachers.html', context)


class CreateTeacherView(LoginRequiredMixin, CreateView):
    model = Teachers
    template_name = 'vrtic/create_teacher.html'
    fields = '__all__'
    login_url = 'vrtic:login'
    success_url = reverse_lazy('vrtic:teachers_centralni')

    def get_context_data(self, **kwargs):
        kwargs['groups'] = Group.objects.all()
        return super(CreateTeacherView, self).get_context_data(**kwargs)


class TeacherUpdateView(LoginRequiredMixin, UpdateView):
    model = Teachers
    fields = '__all__'
    template_name = 'vrtic/teacher_update.html'
    context_object_name = 'teacher'
    login_url = 'vrtic:login'
    success_url = reverse_lazy('vrtic:teachers_centralni')

    def get_context_data(self, **kwargs):
        kwargs['groups'] = Group.objects.all()
        return super(TeacherUpdateView, self).get_context_data(**kwargs)


def delete_teacher(request, pk):
    teacher = Teachers.objects.get(id=pk)
    if request.method == 'POST':
        teacher.delete()
        return redirect('vrtic:teachers_centralni')
    context = {
        'teacher': teacher
    }
    return render(request, 'vrtic/modal_delete_teacher.html', context)


@login_required(login_url='vrtic:login')
def create_payment(request, pk):
    kid = Kids.objects.get(id=pk)
    payments = Payment.objects.filter(user=kid)
    total_payment = payments.aggregate(Sum('paid'))
    amount = total_payment.get('paid__sum')
    payment_form = PaymentForm()

    if request.method == 'POST':
        payment_form = PaymentForm(request.POST)
        if payment_form.is_valid():
            payment = payment_form.save(commit=False)
            payment.user = kid
            payment_form.save()
            return redirect('vrtic:create_payment', pk=pk)

    context = {
        'payment_form': payment_form,
        'kid': kid,
        'payments': payments,
        'amount': amount,
    }
    return render(request, 'vrtic/create_payment.html', context)


@login_required(login_url='vrtic:login')
def update_payment(request, pk):
    payment = Payment.objects.get(id=pk)
    update_form = UpdatePaymentForm(instance=payment)
    if request.method == 'POST':
        update_form = UpdatePaymentForm(request.POST, instance=payment)
        if update_form.is_valid():
            update_form.save()
            return redirect('vrtic:create_payment', pk=payment.user.id)

    context = {
        'update_form': update_form,
        'payment': payment
    }
    return render(request, 'vrtic/modal2.html', context)


@login_required(login_url='vrtic:login')
def delete_payment(request, pk):
    payment = Payment.objects.get(id=pk)
    kid = payment.user.id
    if request.method == 'POST':
        payment.delete()
        return redirect('vrtic:create_payment', pk=kid)

    context = {
        'payment': payment
    }
    return render(request, 'vrtic/modal_delete_payment.html', context)


@login_required(login_url='vrtic:login')
def groups_centralni(request):
    groups = Group.objects.filter(name__icontains='centralni')
    name = 'Centralni Vrtić'

    context = {
        'groups': groups,
        'name': name,
    }
    return render(request, 'vrtic/groups.html', context)


@login_required(login_url='vrtic:login')
def groups_novi(request):
    groups = Group.objects.filter(name__icontains='novi')
    name = 'Novi Vrtić'

    context = {
        'groups': groups,
        'name': name,
    }
    return render(request, 'vrtic/groups.html', context)


@login_required(login_url='vrtic:login')
def groups_tq(request):
    groups = Group.objects.filter(name__icontains='tq')
    name = 'Vrtić TQ'

    context = {
        'groups': groups,
        'name': name,
    }
    return render(request, 'vrtic/groups.html', context)


@login_required(login_url='vrtic:login')
def groups_stefan(request):
    groups = Group.objects.filter(name__icontains='stefan')
    name = 'Sveti Stefan Vrtić'

    context = {
        'groups': groups,
        'name': name,
    }
    return render(request, 'vrtic/groups.html', context)


@login_required(login_url='vrtic:login')
def groups_petrovac(request):
    groups = Group.objects.filter(name__icontains='petrovac')
    name = 'Petrovac Vrtić'

    context = {
        'groups': groups,
        'name': name,
    }
    return render(request, 'vrtic/groups.html', context)


@login_required(login_url='vrtic:login')
def group_view(request, id):
    groups = Group.objects.all()
    group = Group.objects.get(id=id)
    kids = Kids.objects.filter(group=group)
    kids_num = kids.filter().count()
    male = kids.filter(gender='muski').count()
    female = kids.filter(gender='zenski').count()

    context = {
        'groups': groups,
        'group': group,
        'kids': kids,
        'kids_num': kids_num,
        'male': male,
        'female': female,

    }
    return render(request, 'vrtic/group.html', context)


@login_required(login_url='vrtic:login')
def search_bar(request):
    search = request.GET.get('search')
    kids = Kids.objects.filter(name__icontains=search)
    if not kids:
        messages.info(request, 'Pretraga neuspjesna')
        return redirect('vrtic:kids')

    context = {
        'kids': kids
    }
    return render(request, 'vrtic/kids_list.html', context)


@login_required(login_url='vrtic:login')
def all_payments(request):
    payments = Payment.objects.all()
    if request.method == 'POST':
        search = request.POST.get('search_payments')
        payments = Payment.objects.filter(payment_date__icontains=search)
        if not payments:
            messages.info(request, 'Neuspjesna pretraga')
            return redirect('vrtic:all_payments')

        return render(request, 'vrtic/all_payments.html', {'payments': payments})

    context = {
        'payments': payments
    }
    return render(request, 'vrtic/all_payments.html', context)
