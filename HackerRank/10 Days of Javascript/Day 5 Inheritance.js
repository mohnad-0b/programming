class Rectangle {
    constructor(w, h) {
        this.w = w;
        this.h = h;
    }
}
class Square{
    constructor(w) {
        this.area = function() {return w*w } ;   
    }
}
Rectangle.prototype.area = function() { return this.w*this.h}


if (JSON.stringify(Object.getOwnPropertyNames(Square.prototype)) === JSON.stringify([ 'constructor' ])) {
    const rec = new Rectangle(3, 4);
    const sqr = new Square(3);
    
    console.log(rec.area());
    console.log(sqr.area());
} else {
    console.log(-1);
    console.log(-1);
}