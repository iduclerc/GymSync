describe('template spec', () => {
    it('teste 1 add exercicio', () => {
  
      cy.visit('http://127.0.0.1:8000/treino/75/add_exercicio/')
      
      cy.wait(1000) // espera 3s
      cy.get('#treino1').type('treino 1')
      cy.wait(1000)
      cy.get('#repeticoes1').type(12)
      cy.wait(1000)
      cy.get('#carga1').type(48)
      cy.get(':nth-child(1) > form > .btn').click()
    })
    it('teste 2 add exercicio', () => {
  
        cy.visit('http://127.0.0.1:8000/treino/75/add_exercicio/')
        cy.wait(1000) // espera 3s
        cy.get('#treino1').type('treino 1')
        cy.wait(1000)
        //cy.get('#repeticoes1').type(12)
        cy.wait(1000)
        cy.get('#carga1').type(48)
        cy.get(':nth-child(1) > form > .btn').click()
      })
  })