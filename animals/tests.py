from django.test import TestCase, RequestFactory

from animals.models import Animal, Breed, Food, Brand

from django.core.urlresolvers import reverse


def create_animal():
    """
    Creates an animal to test against.
    """
    return


class AnimalsViewTests(TestCase):
    """
    View Tests
    """

    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.breed = Breed.objects.create(
            name='Breed',
            url=""
        )
        self.animal = Animal.objects.create(
            breed=self.breed,
            name="AnimalName",
            birth_date="2001-01-01",
            microchip_id='123456',
            about="about",
            private=False,
            live=True,
        )

    def test_index_view_with_no_animals(self):
        """
        If no animals exist, an appropriate message should be displayed.
        """
        Animal.objects.all().delete()
        response = self.client.get(reverse('animals:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No Animals")
        self.assertQuerysetEqual(response.context['animals'], [])

    def test_index_view_returns_animals(self):
        """
        Should return one animal
        """
        response = self.client.get(reverse('animals:index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['animals'], ['<Animal: AnimalName>'])

    def test_index_should_only_return_live_animals(self):
        """
        Should return one animal
        """
        self.animal2 = Animal.objects.create(
            breed=self.breed,
            name="DeadFred",
            birth_date="2001-01-01",
            microchip_id='123456',
            about="about",
            private=False,
            live=False,
        )
        response = self.client.get(reverse('animals:index'))
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "DeadFread")
        self.assertContains(response, "AnimalName")
        self.assertEqual(len(response.context['animals']), 1)

    def test_details_view_with_invalid_id(self):
        """
        Invalid ID should return 404
        """
        response = self.client.get(reverse('animals:detail', args=(9999,)))
        self.assertEqual(response.status_code, 404)

    def test_details_view_with_valid_id(self):
        """
        Valid ID should return 200
        """
        response = self.client.get(reverse('animals:detail', args=(1,)))
        self.assertEqual(response.status_code, 200)

    def test_detail_view_returns_correct_animal(self):
        """
        Valid ID should return corresponding animal
        """
        response = self.client.get(reverse('animals:detail', args=(1,)))
        self.assertContains(response, "AnimalName")

    def test_update_view_with_invalid_id(self):
        """
        Invalid ID should return 404
        """
        response = self.client.get(reverse('animals:update', args=(9999,)))
        self.assertEqual(response.status_code, 404)

    def test_update_view_with_valid_id(self):
        """
        Valid ID should return 200
        """
        response = self.client.get(reverse('animals:update', args=(1,)))
        self.assertEqual(response.status_code, 200)

    def test_update_view_returns_correct_animal(self):
        """
        Valid ID should return corresponding animal
        """
        response = self.client.get(reverse('animals:update', args=(1,)))
        self.assertContains(response, "AnimalName")

    def test_delete_view_with_invalid_id(self):
        """
        Invalid ID should return 404
        """
        response = self.client.get(reverse('animals:delete', args=(9999,)))
        self.assertEqual(response.status_code, 404)


class AnimalsModelTests(TestCase):
    """
    Model Tests
    """

    def setUp(self):
        """
        Test Setup
        :return:
        """
        self.factory = RequestFactory()
        self.breed = Breed.objects.create(
            name='BreedName',
            url="http://www.google.com"
        )
        self.brand = Brand.objects.create(
            name='BrandName',
            url='http://www.google.com'
        )
        self.food = Food.objects.create(
            brand=self.brand,
            name='FoodName',
            upc='123456'
        )
        self.animal = Animal.objects.create(
            #user=self.user,
            breed=self.breed,
            name="AnimalName",
            birth_date="2001-01-01",
            microchip_id='123456',
            about="about",
            private=False,
            live=True,
        )

    def test_animal_soft_delete(self):
        """
        Test Animal Soft Delete
        :return: None
        """
        self.assertEqual(self.animal.name, "AnimalName")
        self.assertTrue(self.animal.live)

        self.animal.delete()

        self.assertIsNotNone(self.animal)
        self.assertFalse(self.animal.live)
        self.assertEqual(self.animal.name, "AnimalName")

    def test_breed_soft_delete(self):
        """
        Test Breed Soft Delete
        :return: None
        """
        self.assertEqual(self.breed.name, "BreedName")
        self.assertTrue(self.breed.live)

        self.breed.delete()

        self.assertIsNotNone(self.breed)
        self.assertFalse(self.breed.live)
        self.assertEqual(self.breed.name, "BreedName")

    def test_food_soft_delete(self):
        """
        Test Food Soft Delete
        :return: None
        """
        self.assertEqual(self.food.name, "FoodName")
        self.assertTrue(self.food.live)

        self.food.delete()

        self.assertIsNotNone(self.food)
        self.assertFalse(self.food.live)
        self.assertEqual(self.food.name, "FoodName")

    def test_food_soft_delete(self):
        """
        Test Brand Soft Delete
        :return: None
        """
        self.assertEqual(self.brand.name, "BrandName")
        self.assertTrue(self.brand.live)

        self.brand.delete()

        self.assertIsNotNone(self.brand)
        self.assertFalse(self.brand.live)
        self.assertEqual(self.brand.name, "BrandName")

    def test_breed_wiki_link_url(self):
        """
        Test Brand Soft Delete
        :return: None
        """
        self.assertEqual("http://www.wikipedia.com/wiki/BreedName", self.animal.breed.wiki_link())
