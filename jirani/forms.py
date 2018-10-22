from .models import Article
#......
class NewNeighbourhoodForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        exclude = ['editor', 'pub_date']
        