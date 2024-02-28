import { Request, Response } from "express";
import { CreateOrderService } from "../../services/order/CreateOrderService";

class CreateOrderController{
    async handle(req: Request, res: Response){

        //post e put: req.body
        const {name, date, time} = req.body;

        const createOrderService = new CreateOrderService();

        const order = await createOrderService.execute({
            name,
            date,
            time
        });
        return res.json(order)

    }
}

export {CreateOrderController}