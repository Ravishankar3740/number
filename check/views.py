from django.shortcuts import render

# Create your views here.

def check(request):
    
    if request.method == 'GET':
        return render(request,"check/check.html")
    else:
        number = request.POST.get('Mobile_no')
        temp = 0
        for i in str(number):
            temp = int(i)+temp

        final = 0
        next_final = 0
        for i in str(temp):
            final = int(i)+final
        print(final)
        if len(str(final)) == 1:
            if final == 5:
                print("You can take this sim")
                return render(request,"check/final.html")
            else:
                print("Dont take")
                return render(request,"check/reject.html")
        else:
            for i in str(final):
                next_final = int(i)+next_final
            print(next_final)
            if next_final == 5:
                print("You can take this sim")
                return render(request,"check/final.html")
            else:
                print("Dont take")
                return render(request,"check/reject.html")

        