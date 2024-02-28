/*
  Warnings:

  - You are about to drop the column `data` on the `orders` table. All the data in the column will be lost.

*/
-- AlterTable
ALTER TABLE "orders" DROP COLUMN "data",
ADD COLUMN     "date" TEXT,
ADD COLUMN     "time" TEXT;
