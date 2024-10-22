describe('template spec', () => {
    it('teste 1 filtrar treino', () => {
        cy.visit('http://127.0.0.1:8000/treino/64/add_exercicio/')
        cy.wait(2000)
        cy.get('#filtro').select('Costas')
        cy.wait(2000)
        cy.get('#repeticoes2').type(10)
        cy.wait(2000)
        cy.get('#carga2').type(80)
        cy.wait(2000)
        cy.get('[data-grupo="Costas"] > form > .btn').click()
        cy.wait(2000)
    })
  })