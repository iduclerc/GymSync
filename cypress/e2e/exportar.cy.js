describe('template spec', () =>{
    it('teste exportar', () =>{
        cy.visit('http://127.0.0.1:8000/exportar_treino/')
        cy.wait(1000)
        cy.get('#treino').select('treino 1')
        cy.wait(1000)
        cy.get('.btn').click()
        cy.wait(1000)
    })

    it('teste exportar NF', () =>{
        cy.visit('http://127.0.0.1:8000/exportar_treino/')
        cy.wait(1000)
        cy.get('#treino').select('treino inexistente')
        cy.wait(1000)
        cy.get('.btn').click()
        cy.wait(1000)
        //Caso haja a tentativa de acessar um treino inexistente, vai dar erro (Explocação da hora do screencast)
    })
})