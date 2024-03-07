-- CreateTable
CREATE TABLE "performance" (
    "id" TEXT NOT NULL,
    "aluno_id" INTEGER NOT NULL,
    "username" TEXT NOT NULL,
    "date" TIMESTAMP(3) NOT NULL,
    "count" INTEGER NOT NULL,
    "des" DECIMAL(65,30) NOT NULL,
    "key" TEXT NOT NULL,

    CONSTRAINT "performance_pkey" PRIMARY KEY ("id")
);
