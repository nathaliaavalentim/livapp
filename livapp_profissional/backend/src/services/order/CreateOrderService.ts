import prismaClient from "../../prisma";

interface OrderRequest{
    name_product: string,
    product_id: string,
    dateSession: string,
    schedule: string
}

class CreateOrderService{
    async execute({ name_product, product_id, dateSession, schedule }: OrderRequest){
console.log(name_product, product_id, dateSession)
console.log("AQUIIII")
        const order = await prismaClient.order.create({
            data:{
                name_product: name_product,
                product_id: product_id, 
                dateSession: dateSession, 
                schedule: schedule
            }
        })

        return order;
    }
}

export { CreateOrderService }