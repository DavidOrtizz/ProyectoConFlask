import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import * as config from '../../assets/config.json';
import { lastValueFrom } from 'rxjs';
import { Operario } from '../Model/operario';
import { Pedido } from '../Model/pedido';

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


  // Peticiones PEDIDO
  async getListaPedidos() {
    const request$ = await this.http.get(this.url + "/operario");
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

    const request$ = await this.http.post(this.url + "/pedido", JSON.stringify(pedido), options);
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

    const request$ = await this.http.put(this.url + "/pedido/" + pedido.PedidoID, JSON.stringify(pedido), options);
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

    const request$ = await this.http.delete(this.url + "/pedido/" + id, options);
    await lastValueFrom(request$)
  }
}
