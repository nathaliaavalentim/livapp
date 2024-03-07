/*
  Warnings:

  - You are about to drop the column `product_id` on the `orders` table. All the data in the column will be lost.
  - The `dateSession` column on the `orders` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - A unique constraint covering the columns `[description,name]` on the table `products` will be added. If there are existing duplicate values, this will fail.
  - Added the required column `description` to the `orders` table without a default value. This is not possible if the table is not empty.

*/
-- DropForeignKey
ALTER TABLE "orders" DROP CONSTRAINT "orders_product_id_name_product_fkey";

-- DropIndex
DROP INDEX "products_id_name_key";

-- AlterTable
ALTER TABLE "orders" DROP COLUMN "product_id",
ADD COLUMN     "description" TEXT NOT NULL,
DROP COLUMN "dateSession",
ADD COLUMN     "dateSession" TIMESTAMP(3) DEFAULT CURRENT_TIMESTAMP;

-- CreateIndex
CREATE UNIQUE INDEX "products_description_name_key" ON "products"("description", "name");

-- AddForeignKey
ALTER TABLE "orders" ADD CONSTRAINT "orders_description_name_product_fkey" FOREIGN KEY ("description", "name_product") REFERENCES "products"("description", "name") ON DELETE RESTRICT ON UPDATE CASCADE;
