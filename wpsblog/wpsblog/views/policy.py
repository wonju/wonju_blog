from django.shortcuts import render


def disclaimer(request):
    return render(
        request,
        "policy/disclaimer.html",
        {},
    )


def terms(request):
    return render(
        request,
        "policy/terms.html",
        {},
    )


def privacy(request):
    return render(
        request,
        "policy/privacy.html",
        {},
    )
