"""
Books - Views.py

Basic json based interfaces for getting information on a book or chapter

"""
from django.http import HttpResponse
from django.utils import simplejson
from books.models import Book, Chapter
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

#outbound json service
# books:
#  title:
#  tagline:
#  id:
def list(request):
	book_list = Book.objects.all()
	to_json = {'books':[]}
	for book in book_list:
		to_json["books"].append({'title':book.title, 'tagline':book.tagline, 'id':str(book.id)})

	#to_json = serializers.serialize('json', book_list, fields=('title','tagline'))
	return HttpResponse(simplejson.dumps(to_json), mimetype='application/json')

#inbound json message
@csrf_exempt	
def new_book(request):
	#try to make a new book with the passed in data
	if request.POST:
		print 'Raw Data: "%s"' % request.raw_post_data 
		json_data = simplejson.loads(request.raw_post_data)
	
	if json_data:
		#try to create our chapter now
		newBook = Book(title=json_data['title'],tagline=json_data['tagline'])
		newBook.save()	
		newChapter = Chapter(title=json_data['chapter title'], story=json_data['chapter story'], book=newBook)
		newChapter.save()
		to_json = { 'success' : True, 'Book ID' : str(newBook.id) }
	else:
		to_json = { 'success' : False }
		
	return HttpResponse(simplejson.dumps(to_json), mimetype='application/json')
	
#inbound json message	
@csrf_exempt	
def add_chapter(request, book_id, chapter_id):
	if request.POST:
		print 'Raw Data: "%s"' % request.raw_post_data 
		json_data = simplejson.loads(request.raw_post_data)
	else:
		to_json = {'success' : False }
		return HttpResponse(simplejson.dumps(to_json), mimetype='application/json')
		
	myBook = Book.objects.get(id=book_id)
	parentChap = Chapter.objects.get(id=chapter_id)
		
	newChapter = Chapter(title=json_data['title'], story=json_data['story'], book=myBook, parentChapter=parentChap)
	newChapter.save()
	to_json = { 'success' : True, 'Chapter ID' : str(newChapter.id) }
				
	return HttpResponse(simplejson.dumps(to_json), mimetype='application/json')		
		
def chapter(request, book_id, chapter_id):
	try:
		myChapter = Chapter.objects.get(id=chapter_id)
	except:
		to_json = {"success":False}
		return HttpResponse(simplejson.dumps(to_json), mimetype='application/json')
	
	to_json = {'title':myChapter.title, 'story':myChapter.story, 'id':str(myChapter.id), 'children':[]}
	
	options = Chapter.objects.filter(parentChapter=myChapter)	
	for option in options:
		to_json["children"].append({'title':option.title, 'id':str(option.id)})
		
	return HttpResponse(simplejson.dumps(to_json), mimetype='application/json')	

def chapterOne(request, book_id):
	chapter_id = 1
	try:
		chapterOne = Chapter.objects.get(book=book_id,parentChapter__isnull=True)
	except:		
		to_json = {"success":False}
		return HttpResponse(simplejson.dumps(to_json), mimetype='application/json')
		
	to_json = {'title':chapterOne.title, 'story':chapterOne.story}			
	return chapter(request, book_id, chapterOne.id)
