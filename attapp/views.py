from django.shortcuts import render
from attapp.models import sign,faculty,student,admin,mark,leavefac,leavestu,stud_attendance,timetable
from django.http import HttpResponse
from django.contrib.auth import logout
from django.shortcuts import redirect

# Create your views here.

def display(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        mobile=request.POST.get('mobile')

        a=sign(username=username,email=email,password=password,mobile=mobile)
        a.save()
        return render(request,'index.html')

def signupfac(request):
    if request.method=='POST':
        Fid=request.POST.get('Fid')
        Name=request.POST.get('Name')
        Address=request.POST.get('Address')
        DOB=request.POST.get('DOB')
        Gender=request.POST.get('Gender')
        Qualification=request.POST.get('Qualification')
        Mobile=request.POST.get('Mobile')
        BatchInCharge=request.POST.get('BatchInCharge')
        Email=request.POST.get('Email')
        Password=request.POST.get('Password')

        b=faculty(Fid=Fid,Name=Name,Address=Address,DOB=DOB,Gender=Gender,Qualification=Qualification,Mobile=Mobile,BatchInCharge=BatchInCharge,Email=Email,Password=Password)
        b.save()
        return render(request,'faculty_signup.html')

def signupstud(request):
    if request.method=='POST':
        Sid=request.POST.get('Sid')
        AdmNo=request.POST.get('AdmNo')
        AdmDate=request.POST.get('AdmDate')
        Name=request.POST.get('Name')
        Address=request.POST.get('Address')
        DOB=request.POST.get('DOB')
        Gender=request.POST.get('Gender')
        Mobile=request.POST.get('Mobile')
        Guardian=request.POST.get('Guardian')
        Batch=request.POST.get('Batch')
        Email=request.POST.get('Email')
        Password=request.POST.get('Password')

        c=student(Sid=Sid,AdmNo=AdmNo,AdmDate=AdmDate,Name=Name,Address=Address,DOB=DOB,Gender=Gender,Mobile=Mobile,Guardian=Guardian,Batch=Batch,Email=Email,Password=Password)
        c.save()
    return render(request,'student_signup.html')



def authentication(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        username=str(username)
        password=str(password)
        u=admin.objects.filter(username=username,password=password)
        if(u.count()==1):
            return render(request,'adminhome.html')
        else:
            us=faculty.objects.filter(Name=username,Password=password)
            if us.count()==1:
                request.session['usrnm']=username
                q=faculty.objects.all().filter(Name=username)[0]
                request.session['btch']=q.BatchInCharge
                request.session['fid']=q.Fid
                return render(request,'facultyhome.html')
            else:
                usr=student.objects.filter(Name=username,Password=password)
                if(usr.count()==1):
                    request.session['usernm']=username
                    qry=student.objects.all().filter(Name=username)[0]
                    request.session['sid']=qry.Sid
                    request.session['batch']=qry.Batch
                    return render(request,'studenthome.html')
                else:
                    return HttpResponse('Login Unsuccessful')

def viewfacpro(request):
    queryset1=faculty.objects.filter(Name=request.session['usrnm'])
    return render(request,'fac_profile.html',{'authors1':queryset1})

def viewstudpro(request):
    queryset=student.objects.all().filter(Name=request.session['usernm'])
    return render(request,'stud_profile.html',{'authors':queryset})


def viewstud(request):
    queryset=student.objects.all()
    return render(request,'stu_details.html',{'authors':queryset})

    
def viewstdnt(request):
    queryset=student.objects.all().filter(Batch=request.session['btch'])
    return render(request,'view_student.html',{'authors':queryset})

def viewfac(request):
    queryset=faculty.objects.all()
    return render(request,'fac_details.html',{'authors':queryset})

def get_stuid(request):
    queryset=student.objects.all().filter(Batch=request.session['btch'])
    return render(request,'view_mark.html',{'authors':queryset})

def getsid(request):
    qr=student.objects.all().filter(Batch=request.session['btch'])
    return render(request,'view_studattndc.html',{'author':qr})


def addmark(request):
    if request.method=='POST':
        Sid=request.POST.get('Sid')
        AssmntNo=request.POST.get('AssessmentNo')
        Sub1=request.POST.get('sub1')
        Sub2=request.POST.get('sub2')
        Sub3=request.POST.get('sub3')
        #Percentage=((S1+S2+S3)/60)*100

        c=mark(AssessmentNo=AssmntNo,Sub1=Sub1,Sub2=Sub2,Sub3=Sub3,Sid=Sid)
        c.save()
    return render(request,'view_mark.html')  


def viewstudmark(request):
    querysett=mark.objects.all().filter(Sid=request.session['sid'])
    return render(request,'viewmymark.html',{'authorss':querysett})



def fid(request):
    queryset=faculty.objects.all().filter(Fid=request.session['fid'])
    return render(request,'fac_applyleave.html',{'authors':queryset})

def facleave(request):
    if request.method=='POST':
        fid=request.POST.get('fid')
        fromdate=request.POST.get('fromdate')
        todate=request.POST.get('todate')
        reason=request.POST.get('reason')
        status='Pending'
        #Percentage=((S1+S2+S3)/60)*100

        c=leavefac(Fid=fid,Fromdate=fromdate,Todate=todate,Reason=reason,Status=status)
        c.save()
    return render(request,'fac_applyleave.html') 

def sid(request):
    queryset=student.objects.all().filter(Sid=request.session['sid'])
    return render(request,'stud_applyleave.html',{'authors':queryset})


def stuleave(request):
    if request.method=='POST':
        sid=request.POST.get('sid')
        fromdate=request.POST.get('fromdate')
        todate=request.POST.get('todate')
        reason=request.POST.get('reason')
        status='Pending'
        #Percentage=((S1+S2+S3)/60)*100

        c=leavestu(Sid=sid,Fromdate=fromdate,Todate=todate,Reason=reason,Status=status)
        c.save()
    return render(request,'stud_applyleave.html')



def viewstudlv(request):
    querysettt=leavestu.objects.all().filter(Sid=request.session['sid'])
    return render(request,'stud_applyleave.html',{'authorsss':querysettt})



def studentattendance(request):
    if request.method=='POST':
        sid=request.POST.get('sid')
        date=request.POST.get('date')
        hr1=request.POST.get('hr1')
        hr2=request.POST.get('hr2')
        hr3=request.POST.get('hr3')
        hr4=request.POST.get('hr4')
        btch=request.session['btch']
        

        c=stud_attendance(Sid=sid,Date=date,status_h1=hr1,status_h2=hr2,status_h3=hr3,status_h4=hr4,batch=btch)
        c.save()
    return render(request,'view_studattndc.html')


def facultyleaveview(request):
    queryset=leavefac.objects.all()
    return render(request,'fac_leave.html',{'authors':queryset})

def approvefac(request):
    if request.method=='POST':
        faid=request.POST.get('faid')
        leavefac.objects.filter(Fid=faid).update(Status='Approved')
        return render(request,'fac_leave.html')

def studentleaveview(request):
    queryset=leavestu.objects.all()
    return render(request,'stu_leave.html',{'authors':queryset})

def approvestu(request):
    if request.method=='POST':
        stid=request.POST.get('stid')
        leavestu.objects.filter(Sid=stid).update(Status='Approved')
        return render(request,'stu_leave.html')

def viewstudentattendance(request):
    q=stud_attendance.objects.all().filter()
    return render(request,'stu_attndc.html',{'athr':q})

def viewstudentmark(request):
    qryy=mark.objects.all().filter()
    return render(request,'stu_mark.html',{'authr':qryy})



def viewstudatt(request):
    queryst=stud_attendance.objects.all().filter(Sid=request.session['sid'])
    return render(request,'viewmyattndc.html',{'authr':queryst})

def studtimetable(request):
    q=timetable.objects.all().filter(Batch=request.session['batch'])
    return render(request,'view_studtimetable.html',{'a':q})

def tmtable(request):
    q=timetable.objects.all().filter(Batch=request.session['btch'])
    return render(request,'view_timetable.html',{'a':q})

def timetables(request):
    q=timetable.objects.all().filter()
    return render(request,'timetable.html',{'a':q})

def fac_viewmyleave(request):
    q=leavefac.objects.all().filter(Fid=request.session['fid'])
    return render(request,'fac_appliedleave.html',{'a':q})

def stu_viewmyleave(request):
    q=leavestu.objects.all().filter(Sid=request.session['sid'])
    return render(request,'stu_appliedleave.html',{'a':q})

def editfaculty(request):
    q=faculty.objects.all().filter(Fid=request.session['fid'])
    return render(request,'fac_editprofile.html',{'a':q})

def editfacultyprofile(request):
    if request.method=='POST':
        name=request.POST.get('name')
        address=request.POST.get('address')
        gender=request.POST.get('gender')
        qualification=request.POST.get('qualification')
        mobile=request.POST.get('mobile')
        batch=request.POST.get('batch')
        email=request.POST.get('email')
        password=request.POST.get('password')

        faculty.objects.filter(Fid=request.session['fid']).update(Name=name,Address=address,Gender=gender,Qualification=qualification,Mobile=mobile,BatchInCharge=batch,Email=email,Password=password)
        return redirect('fac_profile')

def editstudent(request):
    q=student.objects.all().filter(Sid=request.session['sid'])
    return render(request,'stud_editprofile.html',{'a':q})    

def editstudentprofile(request):
    if request.method=='POST':
        name=request.POST.get('name')
        address=request.POST.get('address')
        gender=request.POST.get('gender')
        mobile=request.POST.get('mobile')
        guardian=request.POST.get('guardian')
        batch=request.POST.get('batch')
        email=request.POST.get('email')
        password=request.POST.get('password')

        student.objects.filter(Sid=request.session['sid']).update(Name=name,Address=address,Gender=gender,Guardian=guardian,Mobile=mobile,Batch=batch,Email=email,Password=password)
        return redirect('stud_profile')





def logout_view(request):
    logout(request)
    return redirect('login')

