describe('template spec', () =>{
    it('teste avaliar', () =>{
        
        cy.visit('http://127.0.0.1:8000/treino/75/add_exercicio/')
        cy.wait(1000)
        cy.get('#repeticoes1').type(10)
        cy.wait(1000)
        cy.get('#carga1').type(30, {force : true})
        cy.wait(1000)
        cy.get(':nth-child(1) > form > .rating > [for="star1_1"]').click()
        cy.wait(3000)
        cy.get(':nth-child(1) > form > .btn').click()
        cy.wait(1000)
    })
})