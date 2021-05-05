# from django.shortcuts import render
# from itertools import chain
# from django.views.generic import ListView
# from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# from .models import *
#
# class SearchView(ListView):
#     def get(self, request, *args, **kwargs):
#         context = {}
#
#         q = request.GET.get('q')
#         if q:
#             query_sets = []
#
#
#             query_sets.append(Music.objects.search(query=q))
#             query_sets.append(Artist.objects.search(query=q))
#             query_sets.append(Album.objects.search(query=q))
#
#
#
#             final_set = list(chain(*query_sets))
#             final_set.sort(key=lambda instance: instance.pk, reverse=True)
#
#             context['last_question'] = '?q=%s' % query_sets
#
#             current_page = Paginator(final_set, 10)
#
#             page = request.GET.get('page')
#
#             try:
#                 context['object_list'] = current_page.page(page)
#             except PageNotAnInteger:
#                 context['object_list'] = current_page.page(1)
#             except EmptyPage:
#                 context['object_list'] = current_page.page(current_page.num_pages)
#             return render(request=request, template_name=self.template_name,context=context)
