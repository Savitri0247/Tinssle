from django.urls import path
from Influencer.views import InfluencerRegistration, InfluencerProfileView, InfluencerProfileUpdateView, InfluencerPost, InfluencerPostDetailView, InfluencerPostUpdateView, Influencerfollow, InfluencerFollowList
urlpatterns = [
    path('register/', InfluencerRegistration.as_view(), name='register'),
    path('profile/', InfluencerProfileView.as_view(), name='profile'),
    path("update/", InfluencerProfileUpdateView.as_view(), name='update'),
    path('post/', InfluencerPost.as_view(), name="post"),
    path('postdetail/', InfluencerPostDetailView.as_view(), name="postdetail"),
    path('postupdate/', InfluencerPostUpdateView.as_view(), name="postupdate"),
    path('influencerfollow/', Influencerfollow.as_view(), name="influencerfollow"),
    path('influencerfollowlist/', InfluencerFollowList.as_view(),
         name="influencerfollowlist"),
]
