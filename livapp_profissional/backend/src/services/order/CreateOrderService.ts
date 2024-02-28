import prismaClient from "../../prisma";

interface OrderRequest{
    name: string,
    date: string,
    time: string,
}

class CreateOrderService{
    async execute({ name, date, time}: OrderRequest){

        const order = await prismaClient.order.create({
            data:{
                name: name,
                date: date,
                time: time,
            }
        })

        return order;
    }
}

export { CreateOrderService }