import prismaClient from "../../prisma";

interface DetailRequest{
    order_id: string;
}

class DetailsOrdersService{
    async execute({order_id}: DetailRequest){

        const orders = await prismaClient.order.findMany({
            where:{
                id: order_id
            },
            include:{
                products: true,
            }
        })
        return orders;
    }
}

export {DetailsOrdersService}