describe('template spec', () => {
  it('teste 1 criar treino', () => {

    cy.visit('http://localhost:8000/criar_treino')
    cy.wait(3000) // espera 3s
    cy.get('#nome').type('treino 1')
    cy.get('#numero_series').type(3)
    cy.get('#agrupamento_muscular').select('Costas')
    cy.get('.btn').click()
  })
  it('teste 2 criar treino', () => {

    cy.visit('http://localhost:8000/criar_treino')
    cy.wait(3000) // espera 3s
    cy.get('#nome').type('treino 1')
    //cy.get('#numero_series').type(3)
    cy.get('#agrupamento_muscular').select('Costas')
    cy.get('.btn').click()
  })
})