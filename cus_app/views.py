from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from .models import Customer

# Create your views here.

class Index(View):
    def get(self, request):

        return render(request, 'index.html')

    def post(self, request):
        id_cus = request.POST.get('cosid')

        global det_cust
        det_cust = Customer.get_customer_by_id(id_cus)
        print(det_cust)
        message = None
        # value =
        if not det_cust:
            message = "Enter the correct Customer ID !!"
            return render(request, 'index.html',{'message':message,'id':id_cus})
        else:
            cus_name = det_cust.name
            cus_phn = det_cust.phone_no
            cus_email = det_cust.email_id
            cus_area = det_cust.area
            cus_fam_num = det_cust.family_mem
            cus_mem_name = det_cust.mem_name
            print(det_cust, cus_name, cus_phn, cus_email, cus_area, cus_fam_num,cus_mem_name)
            cus_mem_name = cus_mem_name.split(',')
            chk_b_one = request.POST.get('one')
            chk_b_two = request.POST.get('two')
            chk_b_three = request.POST.get('three')
            chk_b_four = request.POST.get('four')
            if chk_b_one == 'on':
                det_cust.visit_for_Queries = 'Done'
                print(det_cust.visit_for_Queries)

            if chk_b_two == 'on':
                det_cust.surgical_or_consultation = 'Done'
                print(det_cust.surgical_or_consultation)

            if chk_b_three == 'on':
                det_cust.medicine_sold = 'Done'
                print(det_cust.medicine_sold)

            if chk_b_four == 'on':
                det_cust.diagnostic = 'Done'
                print(det_cust.diagnostic)
            det_cust.register()

            value_one = det_cust.visit_for_Queries
            value_two = det_cust.surgical_or_consultation
            value_three = det_cust.medicine_sold
            value_four = det_cust.diagnostic
            dict_na = {'id':id_cus,
                       'customer_name': cus_name,
                       'customer_phone_no':cus_phn,
                       'customer_email':cus_email,
                       'customer_area': cus_area,
                       'customer_family_mem':cus_fam_num,
                       'customer_family_mem_name':cus_mem_name,
                       'value_o': value_one,
                       'value_t':value_two,
                       'value_th':value_three,
                       'value_f':value_four,
                       'sub_mess':'Your Form Has Been Submited'
                                  'THANK YOU'
                       }
            print(dict_na)
            return render(request, 'index.html',dict_na)

def sub_page(request):
    chk_b_one = request.POST.get('one')
    chk_b_two = request.POST.get('two')
    chk_b_three = request.POST.get('three')
    chk_b_four = request.POST.get('four')
    if chk_b_one == 'on':
        det_cust.visit_for_Queries = 'Done'
        print(det_cust.visit_for_Queries)

    if chk_b_two == 'on':
        det_cust.surgical_or_consultation = 'Done'
        print(det_cust.surgical_or_consultation)

    if chk_b_three == 'on':
        det_cust.medicine_sold = 'Done'
        print(det_cust.medicine_sold)

    if chk_b_four == 'on':
        det_cust.diagnostic = 'Done'
        print(det_cust.diagnostic)
    det_cust.register()

    value_one = det_cust.visit_for_Queries
    value_two = det_cust.surgical_or_consultation
    value_three = det_cust.medicine_sold
    value_four = det_cust.diagnostic
    dict_na = {
               'value_o': value_one,
               'value_t': value_two,
               'value_th': value_three,
               'value_f': value_four,
               'sub_mess': 'Your Form Has Been Submited'
                           'THANK YOU'
               }
    print(dict_na)
    return render(request, 'sub_page.html',dict_na)

def okay(request):
    return HttpResponse('pretend-binary-data-here')