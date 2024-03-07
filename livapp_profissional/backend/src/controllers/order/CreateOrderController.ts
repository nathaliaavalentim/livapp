import { Request, Response } from "express";
import { CreateOrderService } from "../../services/order/CreateOrderService";

class CreateOrderController{
    async handle(req: Request, res: Response){

        //post e put: req.body
        const { name_product, product_id, dateSession, schedule} = req.body;

        console.log(req)
        console.log("AQUIIII")

        const createOrderService = new CreateOrderService();

        const order = await createOrderService.execute({
            name_product,
            product_id,
            dateSession,
            schedule
           
        });
        return res.json(order)

    }
}

export {CreateOrderController}

