/*
  Warnings:

  - A unique constraint covering the columns `[id,name]` on the table `products` will be added. If there are existing duplicate values, this will fail.
  - Added the required column `name_product` to the `orders` table without a default value. This is not possible if the table is not empty.

*/
-- DropForeignKey
ALTER TABLE "orders" DROP CONSTRAINT "orders_product_id_fkey";

-- AlterTable
ALTER TABLE "orders" ADD COLUMN     "name_product" TEXT NOT NULL;

-- CreateIndex
CREATE UNIQUE INDEX "products_id_name_key" ON "products"("id", "name");

-- AddForeignKey
ALTER TABLE "orders" ADD CONSTRAINT "orders_product_id_name_product_fkey" FOREIGN KEY ("product_id", "name_product") REFERENCES "products"("id", "name") ON DELETE RESTRICT ON UPDATE CASCADE;
