#include<stdio.h>

int main()
{
  double peso, preco, precoUnitario, valorTotal=0, pesoTotal;

  int qtd=0, maisBarato;

  printf("Digite a quantidade de doces comprados: ");
  scanf("%d", &qtd);

  for(int i = 0; i < qtd; i++)
  {
    printf("Doce %d\n", i+1);
    printf("Informe o Peso (g): ");
    scanf("%lf",&peso);

    printf("Informe o Preço (R$): ");
    scanf("%lf",&preco);
    
    precoUnitario = preco / (peso/1000);

    printf("\nPreço unitario calculado = %.2lf/kg\n", precoUnitario);    

    if(i > 0 && maisBarato < precoUnitario)
    {
        maisBarato = i;
    }
    else
    {
        maisBarato = precoUnitario;
    }

    valorTotal += precoUnitario;
    pesoTotal += peso;
  }

 printf("Dados Finais da compra:\n");
 printf("Produto mais barato: Doce %d\n", maisBarato);
 printf("Foram comprados %.2lf g de doce por R$ %.2lf ", pesoTotal, valorTotal);



 return 0;
}