describe('template spec', () =>{
    it('teste imc', () => {
        cy.visit('http://127.0.0.1:8000/calcular_imc/')
        cy.wait(1000)
        cy.get('#peso').type(80, {force : true})
        cy.wait(1000)
        cy.get('#altura').type(1.80)
        cy.wait(1000)
        cy.get('.btn').click()
        cy.wait(3000)

    })
    it('teste imc NF', () => {
        cy.visit('http://127.0.0.1:8000/calcular_imc/')
        cy.wait(1000)
        cy.get('#peso').type(80, {force : true})
        cy.wait(1000)
        cy.get('.btn').click()
        cy.wait(3000)
    })
})