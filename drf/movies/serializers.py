from  rest_framework import serializers
from .models import Movie,Genre


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["genre"]

class MovieSerializer(serializers.ModelSerializer):
    genre = GenreSerializer()
    class Meta:
        model = Movie
        fields = ["name","year","imdb","genre"]

    def create(self,validated_data):
        genre_name = validated_data.pop("genre")
        genre  = Genre.objects.filter(genre = genre_name["genre"])
        if len(genre) == 0:
            genre = Genre.objects.create(**genre_name)
        else:
            genre = Genre.objects.get(genre = genre_name["genre"])
        movie = Movie.objects.create(**validated_data,genre = genre)
        return movie
    
    def update(self,instance,validated_data):
        instance.name = validated_data.get("name",instance.name)
        instance.imdb = validated_data.get("imdb",instance.imdb)
        instance.year = validated_data.get("year",instance.year)
        genre = validated_data.get("genre",instance.genre)
        if Genre.objects.filter(genre = genre["genre"]).exists():
            genre = Genre.objects.get(genre = genre["genre"])
            instance.genre = genre
        else:
            genre = Genre.objects.create(**genre)
            instance.genre = genre
        instance.save()
        return instance
    
    def validate_imdb(self,value):
        if value>10:
            raise serializers.ValidationError("IMDB rating cant be above 10")
        return value
    



