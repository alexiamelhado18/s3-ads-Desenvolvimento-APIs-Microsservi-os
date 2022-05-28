import requests
import acesso







import unittest

class TestStringMethods(unittest.TestCase):


    def test_000_leciona(self):
        r = requests.get('http://localhost:5000/leciona/1/1/')
        self.assertEqual(r.status_code,200)
        try:
            r.json()
        except:
            self.fail('eu esperava um json, mas nao recebi')
        self.assertEqual(r.json(),{'leciona':True,'isok':True})
        r = requests.get('http://localhost:5000/leciona/2/1/')
        self.assertEqual(r.json(),{'leciona':False,'isok':True})
        r = requests.get('http://localhost:5000/leciona/2/3/')
        self.assertEqual(r.json(),{'leciona':True,'isok':True})

    
    def test_001a_leciona_not_found(self):
        r = requests.get('http://localhost:5000/leciona/1/100/')
        self.assertEqual(r.status_code,404)
    
    def test_001b_leciona_not_found(self):
        r = requests.get('http://localhost:5000/leciona/1/200/')
        self.assertEqual(r.status_code,404)
        self.assertEqual(r.json()['isok'],False)
        self.assertEqual(r.json(),{'isok':False, 'erro':'disciplina nao encontrada'})
    
    def test_002a_metodo_leciona(self):
        self.assertEqual(acesso.leciona(id_professor=1,id_disciplina=1),True)
        self.assertEqual(acesso.leciona(id_professor=100,id_disciplina=1),False)
    
    def test_002b_metodo_leciona_disciplina_inexistente(self):
        self.assertEqual(acesso.leciona(id_professor=1,id_disciplina=200),(False,'disciplina inexistente'))
    
    def test_003_atividade(self):
        r = requests.get('http://localhost:5050/atividade/1/?id_professor=1')
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['atividade']['enunciado'], "crie um app de todo em flask")
        self.assertEqual(r.json()['isok'], True)
        r = requests.get('http://localhost:5050/atividade/2/?id_professor=3')
        self.assertEqual(r.json()['atividade']['enunciado'], "crie um servidor que envia email em Flask")
    
    def test_004_atividade_not_found(self):
        r = requests.get('http://localhost:5050/atividade/123/?id_professor=2')
        self.assertEqual(r.json()['isok'], False)
        self.assertEqual(r.status_code,404)
    
    def test_005a_atividade_url(self):
        r = requests.get('http://localhost:5050/atividade/1/?id_professor=1')
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['atividade']['url'], "/atividade/1/")
        r = requests.get('http://localhost:5050/atividade/2/?id_professor=3')
        self.assertEqual(r.json()['atividade']['enunciado'], "crie um servidor que envia email em Flask")
        self.assertEqual(r.json()['atividade']['url'], "/atividade/2/")
    
    def test_005b_atividade_url(self):
        r = requests.get('http://localhost:5050/atividade/1/?id_professor=1')
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['atividade']['url'], "/atividade/1/")
        r = requests.get('http://localhost:5050/atividade/2/?id_professor=3')
        self.assertEqual(r.json()['atividade']['enunciado'], "crie um servidor que envia email em Flask")
        self.assertEqual(r.json()['atividade']['url'], "/atividade/2/")
        #aqui está a diferença com o anterior
        r = requests.get('http://localhost:5050/atividades/ver_tudo/')
        lista_atividades = r.json()
        primeira_atividade = lista_atividades[0]
        self.assertEqual("url" in primeira_atividade, False)
        segunda_atividade = lista_atividades[1]
        self.assertEqual("url" in segunda_atividade, False)
        


    def test_006_parametro_de_query(self):
        r = requests.get('http://localhost:5050/atividade/1/?id_professor=100')
        self.assertTrue('id_professor' in r.json())
        #sua resposta pode ser uma string ou um numero, eu nao ligo
        self.assertIn(r.json()['id_professor'],[100,'100'])
    
    def test_007a_professor_que_nao_leciona_nao_tem_acesso_as_respostas(self):
        r = requests.get('http://localhost:5050/atividade/1/?id_professor=100')
        #o requests sabe montar query string (a parte ?id_professor=100). Mas resolvi montar a URL na mão pra
        #ficar mais claro pra voces qual era a URL
        # O jeito mais certo segue abaixo
        #r = requests.get('http://localhost:5050/atividade/1/', params={'id_professor':100})
        self.assertFalse('respostas' in r.json()['atividade'])


    
    def test_007b_professor_que_leciona_tem_acesso_as_respostas(self):
        r = requests.get('http://localhost:5050/atividade/1/?id_professor=1')
        #o requests sabe montar query string (a parte depois da "?"). Mas resolvi montar a URL na mão pra
        #ficar mais claro pra voces qual era a URL
        # O jeito mais certo segue abaixo
        #r = requests.get('http://localhost:5050/atividade/1/', params={'id_professor':1})
        if ('respostas' not in r.json()['atividade']):
            self.fail('''passei um professor válido e nao recebi as respostas da atividade. De uma lida no cod do teste para ter dicas''')
        #se voce tomou esse self.fail, talvez voce montou sua resposta incorretamente.
        #Mas tem outro erro comum, mais sutil, que pode ter acontecido:
        # Ao preparar o dicionário do teste anterior, que realmente nao deve ter respostas,
        # talvez voce removeu as respostas do 'banco de dados'.
        # Nesse caso, voce achou que só ia alterar o dicionário que ia enviar,
        # mas acabou alterando o dicionário que estava guardado no servidor
    
    #se nao consta nenhum professor no chamado, novamente nao
    #mandamos as respostas
    def test_007c_request_sem_professor_volta_sem_as_respostas(self):
        r = requests.get('http://localhost:5050/atividade/1/')
        self.assertFalse('respostas' in r.json()['atividade'])

    def test_008a_alunos_e_notas(self):
        r = requests.get('http://localhost:5050/notas/janaina/1/')
        notas = r.json()['notas']
        self.assertEqual(notas, [0,0])
        r = requests.get('http://localhost:5050/notas/cicero/1/')
        notas = r.json()['notas']
        self.assertEqual(notas, [10,10])
        r = requests.get('http://localhost:5050/notas/alexandre/1/')
        notas = r.json()['notas']
        #self.assertEqual(notas, [9,0])
        #queria ter escrito o assert acima, mas vai que voce me devolve em outra ordem?
        self.assertIn(9,notas)
        self.assertIn(0,notas)



    def test_008b_alunos_e_notas(self):
        r = requests.get('http://localhost:5050/notas/miguel/1/')
        notas = r.json()['notas']
        self.assertEqual(notas, [0,0])
        self.assertEqual(r.json()['isok'], True)

    def test_008c_alunos_e_notas_aluno_inexistente(self):
        r = requests.get('http://localhost:5050/notas/diana/1/')
        self.assertEqual(r.json()['isok'], False)
        self.assertEqual(r.status_code,404)


    

def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

runTests()
