# get all favorites by logged user

# "your favorite"  
    user = User.objects.get (request.session['id'])
    Quote.objects.filter(favorited_by=user)

# "quotable quotes"
    Quote.objects.exclude(favorited_by=user)


#add favorite quote
    q= Quote.objects.get(id=quote_id)
    u= User.objects.get(id=request.session[id])
q.favorited_by.add(u)

#remove from favorites
    q= Quote.objects.get(id=quote_id)
    u= User.objects.get(id=request.session[id])
q.favorited_by.remove(u)