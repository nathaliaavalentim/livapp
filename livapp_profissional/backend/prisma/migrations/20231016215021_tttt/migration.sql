/*
  Warnings:

  - A unique constraint covering the columns `[id,name,description]` on the table `products` will be added. If there are existing duplicate values, this will fail.
  - The required column `product_id` was added to the `orders` table with a prisma-level default value. This is not possible if the table is not empty. Please add this column as optional, then populate it before making it required.

*/
-- DropForeignKey
ALTER TABLE "orders" DROP CONSTRAINT "orders_description_name_product_fkey";

-- DropIndex
DROP INDEX "products_description_name_key";

-- AlterTable
ALTER TABLE "orders" ADD COLUMN     "product_id" TEXT NOT NULL;

-- CreateIndex
CREATE UNIQUE INDEX "products_id_name_description_key" ON "products"("id", "name", "description");

-- AddForeignKey
ALTER TABLE "orders" ADD CONSTRAINT "orders_product_id_name_product_description_fkey" FOREIGN KEY ("product_id", "name_product", "description") REFERENCES "products"("id", "name", "description") ON DELETE RESTRICT ON UPDATE CASCADE;
