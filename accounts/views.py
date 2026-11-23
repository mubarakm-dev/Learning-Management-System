from django.shortcuts import render

# Create your views here.


def homeView(request):
    user_name = "Abolaji Lovely"
    courses = ["cyber security", "web dev", "Data science"]
    profile = {
        "name": "John Alabi",
        "course": "cyber security",
        "gender": "Male",
        "active": True

    }
    return render(
        request,
        template_name="accounts/index.html",
        context={
            "userName": user_name, 
            "courses": courses,
            "profile": profile                       
        }
                     
    )

def aboutSection(request):
    return render(request, template_name="accounts/about.html")