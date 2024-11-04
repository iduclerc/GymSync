describe('template spec', () => {
    it('teste 1 add rotina', () => {
  
      cy.visit('http://127.0.0.1:8000/criar_rotina/')
      cy.get('#nome').type('rotina 89')
      cy.wait(1000) // espera 3s
      cy.get('#treino').type('treino 1')
      cy.wait(1000)
      cy.get('#dia_semana').select('Terça-feira')
      cy.wait(1000)
      cy.get('#horario').type('13:00')
      cy.wait(1000)
      cy.get('.btn').click()
      cy.wait(1000)
    })
    
  })