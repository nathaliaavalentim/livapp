/*
  Warnings:

  - The `date` column on the `orders` table would be dropped and recreated. This will lead to data loss if there is data in the column.

*/
-- AlterTable
ALTER TABLE "orders" ALTER COLUMN "table" DROP NOT NULL,
ALTER COLUMN "draft" SET DEFAULT false,
DROP COLUMN "date",
ADD COLUMN     "date" TIMESTAMP(3);
