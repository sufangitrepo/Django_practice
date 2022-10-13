
from heapq import merge
import json
from pickle import TRUE
from django.views import View
from django.http import HttpResponse, JsonResponse, Http404, HttpRequest
from .serializers import AuthorSerializer, BlogSerializer, EntrySerializer
from .models import AuthorModel, BlogModel, EntryModel
from rest_framework.renderers import JSONRenderer 
# Create your views here.


class AuthorView(View):
    user = ''
    
    """
      get method that will return  auhtor/authors as response 
      
    """
    def get(self, request: HttpRequest, id=-1):
        #code for communication with db
        #serializers 
        #JsonRenderer
        #JsonResponse/HttpRespose
        if( id == -1):
            return self.fecthAuthors(request=request)
        else:
            return self.fetchSingleAuthor(id=id, request=request)
    
    
    def fecthAuthors(self, request: HttpRequest,) -> JsonResponse:
        authors = AuthorModel.objects.all()
        data = AuthorSerializer(authors, many=True, )
        rende = JSONRenderer().render(data.data)
        return HttpResponse(rende)
    #JsonResponse(rende,safe=False)
    
   
    def fetchSingleAuthor(self,request: HttpRequest, id: int) -> HttpResponse:
        author = AuthorModel.objects.get(pk=id)
        serializedAuthor = AuthorSerializer(author, many=False)
        jsonData = JSONRenderer().render(serializedAuthor.data)   
        return HttpResponse(jsonData)
        
        
    
class BlogView(View):
    
    def get(self, request: HttpRequest, author_id: int = 0, 
            blog_id: int = 0, id: int=0, ):
        if(author_id > 0):
            return self.fetchBlogs(request, author_id=author_id)
        elif(blog_id > 0):
            return self.fetchSingleBlog(request=request, id=blog_id)
        elif(id > 0):
            return self.fetchBlogs(request=request, author_id=id)
        else:
            return Http404(args='page not found')
        
           
    def fetchBlogs(self, request: HttpRequest, author_id: int) -> HttpRequest:
        blogs = BlogModel.objects.filter(author=author_id)
        serialized_blogs = BlogSerializer(blogs, many=True)
        json_blog = JSONRenderer().render(serialized_blogs.data)
        return HttpResponse(json_blog)
    
    
    def fetchSingleBlog(self, request: HttpRequest, id: int) -> HttpRequest:
        blog = BlogModel.objects.get(pk=id)
        serialized_blog = BlogSerializer(blog, many=False)
        blog_json = JSONRenderer().render(serialized_blog.data)
        dict = json.loads(blog_json)
        blog_id = dict['id']
        detail = EntryModel.objects.get(pk=blog_id)
        serialized_detail = EntrySerializer(detail, many=False)
        json_detail = JSONRenderer().render(serialized_detail.data)
        detail_dict = json.loads(json_detail)  
        json_final = self.merge_two_dicts(dict,detail_dict)  
        return HttpResponse(json.dumps(json_final))
    
    
    
    def merge_two_dicts(self, x, y):
        z = x.copy()   # start with keys and values of x
        z.update(y)    # modifies z with keys and values of y
        return z    
    
    
    """
     post new blog  
    """
    def post(self, request: HttpRequest, id: int) -> HttpRequest:
        return HttpRequest('post of blog with id')
    
    
   