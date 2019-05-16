function shuffle() {
  cartao.forEach(cartao => {
    let ramdomPos = Math.floor(Math.random() * 12);
    cartao.style.order = ramdomPos;
  });
}
