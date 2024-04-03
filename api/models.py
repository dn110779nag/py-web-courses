from tastypie.resources import ModelResource
from shop.models import Category
from shop.models import Course
from tastypie.authorization import Authorization
from .authntication import CustomAuthentication

class CategoryResource(ModelResource):
    class Meta:
        queryset = Category.objects.all()
        resource_name = 'categories'
        allowed_methods = ['get']


class CourseResource(ModelResource):
    class Meta:
        queryset = Course.objects.all()
        resource_name = 'courses'
        allowed_methods = ['get', 'put', 'post', 'delete']
        excludes = ['created_at']
        authentication = CustomAuthentication()
        authorization = Authorization()

    def hydrate(self, bundle):
        bundle.obj.category_id = bundle.data["category_id"]
        return bundle

    def dehydrate(self, bundle):
        bundle.data["category_id"] = bundle.obj.category_id
        bundle.data["category_title"] = bundle.obj.category.title
        return bundle

    def dehydrate_title(self, bundle):
        return bundle.data["title"].upper()
