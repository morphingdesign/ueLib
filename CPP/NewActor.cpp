// -----------------------------------------------------------
// NewActor.cpp
// v.1.0
// Updated: 20211103
// -----------------------------------------------------------

#include "NewActor.h"

// Sets default values
ANewActor::ANewActor()
{
    // Set this actor to call Tick() every frame.  You can turn this off to improve performance if you don't need it.
    PrimaryActorTick.bCanEverTick = true;

}

void ANewActor::OnConstruction()
{
    //ZTestFuncC();
}

// Called when the game starts or when spawned
void ANewActor::BeginPlay()
{
    Super::BeginPlay();

}

void ANewActor::PostRegisterAllComponents()
{
    ZTestFuncC();
    UE_LOG(LogTemp, Warning, TEXT("Post register all components."));

}

// Called every frame
void ANewActor::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

}

// ZTestFuncA
// Convert static mesh components to HISMs, including registering and parenting.
void ANewActor::ZTestFuncA(UHierarchicalInstancedStaticMeshComponent*& NewHISM, FName Name)
{
    UHierarchicalInstancedStaticMeshComponent* HISM;
    NewHISM = NewObject<UHierarchicalInstancedStaticMeshComponent>(this, HISM->StaticClass(), Name);
    NewHISM->SetupAttachment(RootComponent);
    NewHISM->RegisterComponent();
    AddInstanceComponent(NewHISM);
    NewHISM->SetFlags(RF_Transactional);
}

// ZTestFuncC
// Intended to clear static meshes when enabled by user.
void ANewActor::ZTestFuncC() {
}
    if (clearStaticMeshes)
    {
        UE_LOG(LogTemp, Warning, TEXT("Clear Static Meshes is enabled."));
    }
}