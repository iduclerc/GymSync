describe('template spec', () => {
    it('teste 1 excluir treino', () => {
  
      cy.visit('http://127.0.0.1:8000/lista_treino/')
      cy.wait(2000)
      cy.get(':nth-child(1) > form > button').click()
     
    })  
  })