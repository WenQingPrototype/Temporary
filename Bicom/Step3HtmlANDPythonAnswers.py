<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<h1>ResultDisplay</h1>
<form method="post" action="/regedits/">
    {% csrf_token %}
    ward_id =models.IntegerField(max_length=11)
    ward_name =models.IntegerField(max_length=50)
    lga_id =models.IntegerField(max_length=11)
    ward_description = models.CharField(max_length=300)
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateField(verbose_name='date')
    user_ip_address = models.CharField(max_length=50)
    <input type="uniqueid" name="uniqueid" placeholder="uniqueid"/><br>
    <input type="ward_id" name="wardid" placeholder="wardid"/><br>
    <input type="lga_id " name="lgaid" placeholder="lgaid"/><br>
    <input type="ward_description" name="descript" placeholder="descript"/><br>
    <input type="entered_by_user" name="enter" placeholder="enter"/><br>
    <input type="date_entered" name="date" placeholder="date"/><br>
    <input type="user_ip_address " name="address" placeholder="address"/><br>

</form>
</body>
<script>
 
</script>
</html>



'''step 1 '''
obj1 = models.polling_unit.objects.all(lga_id = 25) 
print(ojj1)
'''step 1 '''
total=model.objects.filter(lga_id = xxx).aggregate()
print total
'''step 3'''
def pull_unit_add(request):
    if request.method == "POST":  
        pub_name = request.POST.get('uniqueid')  
        if models.polling_unit.objects.filter(id = uniqueid):
            return render(request, 'publisher_add.html', {'error': "There has been a same person."})
        models.polling_unit.objects.create(id = uniqueid,ward_id = xxxx.........)  
        return redirect('/pull_unit_list/')  
    return render(request, 'pull_unit_add.html')  。
