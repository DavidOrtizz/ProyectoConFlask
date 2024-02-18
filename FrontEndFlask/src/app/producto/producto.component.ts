import { Component } from '@angular/core';
import { APIService } from '../Services/api.service';
import { Producto } from '../Model/producto';

@Component({
  selector: 'app-producto',
  templateUrl: './producto.component.html',
  styleUrls: ['./producto.component.css']
})
export class ProductoComponent {

  listaProductos: Producto[] = [];
  productoPorID: Producto = new Producto;
  productoCrear: Producto = new Producto;
  productoModificar: Producto = new Producto;

  idBuscar: number = 0;
  idBorrar: number = 0;

  constructor(private api: APIService) { }

  async getProductos() {
    this.listaProductos = await this.api.getListaProductos();

  }

  async getProductoPorID() {
    this.productoPorID = await this.api.getProductosPorID(this.idBuscar);

  }

  crearProducto() {
    this.api.crearProducto(this.productoCrear);

  }

  modificarProducto() {
    this.api.modificarProducto(this.productoModificar);

  }

  borrarProducto() {
    this.api.borrarProducto(this.idBorrar);

  }

}
