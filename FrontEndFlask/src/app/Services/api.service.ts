import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import * as config from '../../assets/config.json';
import { lastValueFrom } from 'rxjs';
import { Operario } from '../Model/operario';
import { Pedido } from '../Model/pedido';
import { Producto } from '../Model/producto';
import { Sede } from '../Model/Sede';

@Injectable({
  providedIn: 'root'
})
export class APIService {

  private config: any = config;
  private url: string = '';

  constructor(private http: HttpClient) {
    this.url = this.config.api.host;
  }

  // Peticiones OPERARIO
  // Con el rol Usuario
  async getOperarios() {
    const request$ = await this.http.get(this.url + "/operario");
    let listaOperarios: Operario[] = await lastValueFrom(request$) as Operario[]
    return listaOperarios;
  }

  // Operario por ID
  async getOperarioByID(id: number) {
    const request$ = await this.http.get(this.url + "/operario/" + id);
    let operario: Operario = await lastValueFrom(request$) as Operario
    return operario;
  }

  // Crear Operario
  async crearOperario(operario: Operario) {
    const options: any = {
      headers: new HttpHeaders({
        'Content-Type': 'application/json'
      }),
      responseType: 'text'
    };

    const request$ = await this.http.post(this.url + "/operario", JSON.stringify(operario), options);
    await lastValueFrom(request$)
  }

  // Modificar Operario
  async modificarOperario(operario: Operario) {
    const options: any = {
      headers: new HttpHeaders({
        'Content-Type': 'application/json'
      }),
      responseType: 'text'
    };

    const request$ = await this.http.put(this.url + "/operario/" + operario.ID, JSON.stringify(operario), options);
    await lastValueFrom(request$)
  }

  // Borrar Operario
  async borrarOperario(id: number) {
    const options: any = {
      headers: new HttpHeaders({
        'Content-Type': 'application/json'
      }),
      responseType: 'text'
    };

    const request$ = await this.http.delete(this.url + "/operario/" + id, options);
    await lastValueFrom(request$)
  }

//----------------------------------------------------------------------------------------------------------------------------------------------------
  // Peticiones PEDIDO
  async getListaPedidos() {
    const request$ = await this.http.get(this.url + "/pedidos");
    let listaPedidos: Pedido[] = await lastValueFrom(request$) as Pedido[]
    return listaPedidos;
  }

  // Pedido por ID
  async getPedidoPorID(id: number) {
    const request$ = await this.http.get(this.url + "/pedido/" + id);
    let pedido: Pedido = await lastValueFrom(request$) as Pedido
    return pedido;
  }

  // Crear Pedido
  async crearPedido(pedido: Pedido) {
    const options: any = {
      headers: new HttpHeaders({
        'Content-Type': 'application/json'
      }),
      responseType: 'text'
    };

    const request$ = await this.http.post(this.url + "/crearPedido", JSON.stringify(pedido), options);
    await lastValueFrom(request$)
  }

  // Modificar Pedido
  async modificarPedido(pedido: Pedido) {
    const options: any = {
      headers: new HttpHeaders({
        'Content-Type': 'application/json'
      }),
      responseType: 'text'
    };

    const request$ = await this.http.put(this.url + "/modificaPedido/" + pedido.PedidoID, JSON.stringify(pedido), options);
    await lastValueFrom(request$)
  }

  // Borrar Pedido
  async borrarPedido(id: number) {
    const options: any = {
      headers: new HttpHeaders({
        'Content-Type': 'application/json'
      }),
      responseType: 'text'
    };

    const request$ = await this.http.delete(this.url + "/borrarPedido/" + id, options);
    await lastValueFrom(request$)
  }

  // Peticiones Productos

  async getProductos() {
    const request$ = await this.http.get(this.url + "/producto");
    let listaProductos: Producto[] = await lastValueFrom(request$) as Producto[]
    return listaProductos;
  }

  // Producto por ID
  async getProductosPorID(id: number) {
    const request$ = await this.http.get(this.url + "/producto/" + id);
    let producto: Producto = await lastValueFrom(request$) as Producto
    return producto;
  }

  // Crear Producto
  async crearProducto(producto: Producto) {
    const options: any = {
      headers: new HttpHeaders({
        'Content-Type': 'application/json'
      }),
      responseType: 'text'
    };

    const request$ = await this.http.post(this.url + "/producto", JSON.stringify(producto), options);
    await lastValueFrom(request$)
  }

  // Modificar Producto
  async modificarProducto(producto: Producto) {
    const options: any = {
      headers: new HttpHeaders({
        'Content-Type': 'application/json'
      }),
      responseType: 'text'
    };

    const request$ = await this.http.put(this.url + "/producto/" + producto.ID, JSON.stringify(producto), options);
    await lastValueFrom(request$)
  }

  // Borrar Producto
  async borrarProducto(id: number) {
    const options: any = {
      headers: new HttpHeaders({
        'Content-Type': 'application/json'
      }),
      responseType: 'text'
    };

    const request$ = await this.http.delete(this.url + "/producto/" + id, options);
    await lastValueFrom(request$)
  }


  //Lista de Sedes
  async getSedes() {
    const request$ = await this.http.get(this.url + "/sede");
    let listaSedes: Sede[] = await lastValueFrom(request$) as Sede[]
    console.log(listaSedes)
    return listaSedes;
  }

  // sede por ID
  async getSedeByID(id: number) {
    const request$ = await this.http.get(this.url + "/sede/" + id);
    let sede: Sede = await lastValueFrom(request$) as Sede
    console.log(sede)
    return sede;
  }

  // Crear Sede
  async crearSede(sede: Sede) {
    const options: any = {
      headers: new HttpHeaders({
        'Content-Type': 'application/json'
      }),
      responseType: 'text'
    };
  const request$ = await this.http.post(this.url + "/sede", JSON.stringify(sede), options);
    await lastValueFrom(request$)
  }

  // Modificar Sede
  async modificarSede(sede: Sede) {
    const options: any = {
      headers: new HttpHeaders({
        'Content-Type': 'application/json'
      }),
      responseType: 'text'
    };
 const request$ = await this.http.put(this.url + "/sede/" + sede.ID, JSON.stringify(sede), options);
    await lastValueFrom(request$)
  }

  // Borrar Sede
  async borrarSede(id: number) {
    const options: any = {
      headers: new HttpHeaders({
        'Content-Type': 'application/json'
      }),
      responseType: 'text'
    };
 const request$ = await this.http.delete(this.url + "/sede/" + id, options);
    await lastValueFrom(request$)
}

}
