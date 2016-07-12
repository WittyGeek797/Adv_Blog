from rest_framework.pagination import(
	LimitOffsetPagination,
	PageNumberPagination
)

class PostLimitOffsetPagination(LimitOffsetPagination):
	max_limit = 10
	default_limit = 10

class PagePageNumberPagination(PageNumberPagination):
	page_size = 10