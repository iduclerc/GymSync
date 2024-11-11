describe('template spec', () => {
    it('teste 1 cronometro', () => {
        cy.visit('http://127.0.0.1:8000/treino/75/')
        cy.wait(1000)
        cy.get(':nth-child(1) > .cronometro-container > .start-btn').click()
        cy.wait(5000)
        cy.get(':nth-child(1) > .cronometro-container > .stop-btn').click()
        cy.wait(1000)
        cy.get(':nth-child(1) > .cronometro-container > .reset-btn').click()
        cy.wait(2000)
    })
  })