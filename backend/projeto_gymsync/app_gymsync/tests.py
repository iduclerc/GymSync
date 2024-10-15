from django.test import TestCase
from django.urls import reverse
from app_gymsync.models import Treino  # Importe o modelo de Treino

class CriarTreinoTestCase(TestCase):
    def setUp(self):
        # Configurações iniciais, se necessário (ex: criação de usuários, setup de contexto)
        pass

    def test_criar_treino_com_dados_validos(self):
        # Dados válidos para a criação do treino
        data = {
            'nome': 'Treino A',
            'numero_series': 3,
            'agrupamento_muscular': 'Peito'
        }

        # Faz uma requisição POST para a view de criar treino
        response = self.client.post(reverse('criar_treino'), data)

        # Verifica se a resposta é um redirecionamento (status code 302)
        self.assertEqual(response.status_code, 302)

        # Verifica se o redirecionamento foi para a URL correta ('forum' no seu caso)
        self.assertRedirects(response, reverse('forum'))

        # Verifica se o treino foi salvo no banco de dados
        self.assertTrue(Treino.objects.filter(nome='Treino A').exists())

    def test_criar_treino_com_dados_invalidos(self):
        # Teste com dados incompletos (campo 'nome' vazio)
        data_invalido = {
            'nome': '',  # Campo vazio
            'numero_series': '3',
            'agrupamento_muscular': 'Peito'
        }
        
        # Faz uma requisição POST com dados inválidos
        response = self.client.post(reverse('criar_treino'), data_invalido)

        # Verifica se a página retornou sem redirecionar (status code 200 significa erro de validação)
        self.assertEqual(response.status_code, 200)

        # Verifica que nenhum treino foi criado
        self.assertFalse(Treino.objects.filter(nome='Treino B').exists())

        # Teste com dados incompletos (campo 'agrupamento_muscular' vazio)
        data_invalido = {
            'nome': 'Treino B',
            'numero_series': 4,
            'agrupamento_muscular': ''  # Campo inválido
        }

        # Faz uma requisição POST com dados inválidos
        response = self.client.post(reverse('criar_treino'), data_invalido)

        # Verifica se a página retornou sem redirecionar (status code 200 significa erro de validação)
        self.assertEqual(response.status_code, 200)

        # Verifica que nenhum treino foi criado
        self.assertFalse(Treino.objects.filter(nome='Treino B').exists())