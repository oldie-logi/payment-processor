// types.ts
import { BaseError } from './base-error';

export enum PaymentMethod {
  CreditCard,
  PayPal,
  BankTransfer,
}

export enum PaymentStatus {
  Pending,
  Success,
  Failed,
}

export interface Payment {
  id: string;
  amount: number;
  method: PaymentMethod;
  status: PaymentStatus;
  createdAt: Date;
  updatedAt: Date;
}

export interface PaymentRequest {
  amount: number;
  paymentMethod: PaymentMethod;
}

export class InvalidPaymentMethodError extends BaseError {
  constructor(message: string) {
    super(message);
    this.name = 'InvalidPaymentMethodError';
  }
}