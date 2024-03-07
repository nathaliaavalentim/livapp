/*
  Warnings:

  - A unique constraint covering the columns `[id,name,description]` on the table `products` will be added. If there are existing duplicate values, this will fail.
  - Added the required column `description` to the `orders` table without a default value. This is not possible if the table is not empty.

*/
-- DropForeignKey
ALTER TABLE "orders" DROP CONSTRAINT "orders_product_id_name_product_fkey";

-- DropIndex
DROP INDEX "products_id_name_key";

-- AlterTable
ALTER TABLE "orders" ADD COLUMN     "description" TEXT NOT NULL;

-- AlterTable
ALTER TABLE "products" ALTER COLUMN "description" DROP NOT NULL;

-- CreateIndex
CREATE UNIQUE INDEX "products_id_name_description_key" ON "products"("id", "name", "description");

-- AddForeignKey
ALTER TABLE "orders" ADD CONSTRAINT "orders_product_id_name_product_description_fkey" FOREIGN KEY ("product_id", "name_product", "description") REFERENCES "products"("id", "name", "description") ON DELETE RESTRICT ON UPDATE CASCADE;
