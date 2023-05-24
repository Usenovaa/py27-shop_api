from rest_framework.serializers import ModelSerializer, ValidationError
from .models import Comment, Rating


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'



class RatingSerializer(ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'
    
    def validate_rating(self, rating):
        if rating not in range(1, 6):
            raise ValidationError(
                'Rating must be in range 1 - 6'
            )
        return rating
    
    def validate_product(self, product):
        if self.Meta.model.objects.filter(product=product).exists():
            raise ValidationError(
                'Вы уже оставляли рэйтинг'
            )
        return product
    
