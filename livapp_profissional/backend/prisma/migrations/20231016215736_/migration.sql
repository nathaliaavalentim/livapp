/*
  Warnings:

  - You are about to drop the column `description` on the `orders` table. All the data in the column will be lost.
  - A unique constraint covering the columns `[id,name]` on the table `products` will be added. If there are existing duplicate values, this will fail.

*/
-- DropForeignKey
ALTER TABLE "orders" DROP CONSTRAINT "orders_product_id_name_product_description_fkey";

-- DropIndex
DROP INDEX "products_id_name_description_key";

-- AlterTable
ALTER TABLE "orders" DROP COLUMN "description";

-- CreateIndex
CREATE UNIQUE INDEX "products_id_name_key" ON "products"("id", "name");

-- AddForeignKey
ALTER TABLE "orders" ADD CONSTRAINT "orders_product_id_name_product_fkey" FOREIGN KEY ("product_id", "name_product") REFERENCES "products"("id", "name") ON DELETE RESTRICT ON UPDATE CASCADE;
