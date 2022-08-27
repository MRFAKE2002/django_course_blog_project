from django.test import TestCase
from django.contrib.auth.models import User
from .models import BlogPost
from django.shortcuts import reverse

class BlogPostTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username= 'user1')
        cls.post1 = BlogPost.objects.create(
            title= 'post1',
            text= 'this is a test post1',
            status= BlogPost.STATUS_CHOICES[0][0],
            author= cls.user,
        )
        cls.post2 = BlogPost.objects.create(
            title= 'post2',
            text= 'this is a test post2',
            author= cls.user,
            status= BlogPost.STATUS_CHOICES[1][0],
        )

    def test_post_model_print_str(self):
        self.assertEqual(str(self.post1), self.post1.title)

#___________________________________________________________________________________________________________________________________________
    
    def test_post_detail(self):
        self.assertEqual(self.post1.title, 'post1')
        self.assertEqual(self.post1.text, 'this is a test post1')
        
#___________________________________________________________________________________________________________________________________________
   
    def test_home_post_list_url(self):
        response = self.client.get('/blog/')
        self.assertEquals(response.status_code, 200)

#___________________________________________________________________________________________________________________________________________

    def test_home_post_list_url_by_name(self):
        response= self.client.get(reverse('home_page'))
        self.assertEqual(response.status_code, 200)
  
#___________________________________________________________________________________________________________________________________________
      
    def test_post_title_in_home_page(self):
        response = self.client.get(reverse('home_page'))
        self.assertContains(response, self.post1.title)

#___________________________________________________________________________________________________________________________________________
    
    def test_detail_page_url(self):
        response = self.client.get(f'/blog/{self.post1.id}/')
        self.assertEqual(response.status_code, 200)

#___________________________________________________________________________________________________________________________________________
    
    def test_detail_page_url_by_name(self):
        response = self.client.get(reverse('detail_page', args=[self.post1.id]))
        self.assertEqual(response.status_code, 200) 

#___________________________________________________________________________________________________________________________________________
        
    def test_post_detail_in_detail_page(self):
        response = self.client.get(reverse('detail_page', args=[self.post1.id])) 
        self.assertContains(response, self.post1.title )
        self.assertContains(response, self.post1.text )      

#___________________________________________________________________________________________________________________________________________

    def test_status_404_if_post_id_not_exist(self):
        response = self.client.get(reverse('detail_page', args=[999])) 
        self.assertEqual(response.status_code, 404)
    
#__________________________________________________________________________________________________________________________________________

    def test_draft_post_not_in_home_page(self):    
        response = self.client.get(reverse('home_page')) 
        self.assertContains(response, self.post1.title )
        self.assertNotContains(response, self.post2.title )
        
#___________________________________________________________________________________________________________________________________________

    def test_post_create_page(self):
        response = self.client.post(reverse('create_page'), {
            'title' : 'post create',
            'text' : 'This is a new post',
            'status' : 'pub',
            'author' : self.user.id,
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(BlogPost.objects.last().title, 'post create')
        self.assertEqual(BlogPost.objects.last().text, 'This is a new post')
        
#___________________________________________________________________________________________________________________________________________

    def test_post_update_page(self):
        response = self.client.post(reverse('update_post', args=[self.post2.id]), {
            'title': 'post update',
            'text' : 'This is a post update',
            'author' : self.user.id,
            'status' : 'drf',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(BlogPost.objects.last().title, 'post update')
        self.assertEqual(BlogPost.objects.last().text, 'This is a post update')
                        
#___________________________________________________________________________________________________________________________________________

    def test_post_delete(self):
        response = self.client.post(reverse('delete_post', args=[self.post2.id]))
        self.assertEqual(response.status_code, 302)
                       
#___________________________________________________________________________________________________________________________________________

