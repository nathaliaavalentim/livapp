/*
  Warnings:

  - Changed the type of `aluno_id` on the `performance` table. No cast exists, the column would be dropped and recreated, which cannot be done if there is data, since the column is required.

*/
-- AlterTable
ALTER TABLE "performance" DROP COLUMN "aluno_id",
ADD COLUMN     "aluno_id" INTEGER NOT NULL;
