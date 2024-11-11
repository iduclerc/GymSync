describe('template spec', () => {
  it('teste 1 criar treino', () => {

    cy.visit('http://localhost:8000/criar_treino')
    cy.wait(1000) // espera 3s
    cy.get('#nome').type('treino 1')
    cy.wait(1000)
    cy.get('#numero_series').type(40)
    cy.wait(1000)
    cy.get('#agrupamento_muscular').select('Costas')
    cy.wait(1000)
    cy.get('.btn').click()
  })
  it('teste 2 criar treino', () => {

    cy.visit('http://localhost:8000/criar_treino')
    cy.wait(1000) // espera 3s
    cy.get('#nome').type('treino 1')
    cy.wait(1000)
    //cy.get('#numero_series').type(3)
    cy.get('#agrupamento_muscular').select('Costas')
    cy.wait(1000)
    cy.get('.btn').click()
  })


})